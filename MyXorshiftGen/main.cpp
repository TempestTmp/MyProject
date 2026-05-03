#include <algorithm>
#include <atomic>
#include <iostream>
#include <omp.h>
#include <vector>
#include <fstream>
#include <string>

#include "MyXorshiftGen.cpp"
#include "hit.h"

using namespace std;

// Realisation 1
inline uint32_t single_threaded_implementation(uint32_t number_of_points, const float* axis) {
    uint32_t hit = 0;
    MyXorshiftGen my_xorshift_gen(979, axis);
    for (uint32_t i = 0; i < number_of_points; ++i) {
        if (hit_test(my_xorshift_gen.next_x(), my_xorshift_gen.next_y(), my_xorshift_gen.next_z())) {
            hit += 1;
        }
    }
    return hit;
}

// Get threads
inline int getThreads(int threads) {
    if (threads == -1) {
        threads = omp_get_max_threads();
    }
    return threads;
}

// Сalculates the sum of the coordinates of a vector
inline uint32_t sum(const vector<uint32_t> &my_vector, const int threads) {
    uint32_t hit = 0;
    for (uint32_t i = 0; i < threads; ++i) {
        hit += my_vector[i];
    }
    return hit;
}

// Realisation 2 static
inline uint32_t automatic_multithreaded_static(uint32_t number_of_points, const float* axis, int chunk_size, int threads) {
    threads = getThreads(threads);
    omp_set_num_threads(threads);

    vector<uint32_t> my_vector(threads, 0);
    #pragma omp parallel
    {
        MyXorshiftGen my_xorshift_gen(omp_get_thread_num(), axis);
        uint32_t count = 0;
        #pragma omp for schedule(static, chunk_size)
        for (uint32_t i = 0; i < number_of_points; ++i) {
            if (hit_test(my_xorshift_gen.next_x(), my_xorshift_gen.next_y(), my_xorshift_gen.next_z())) {
                count += 1;
            }
        }
        my_vector[omp_get_thread_num()] = count;
    }
    return sum(my_vector, threads);
}

// Realisation 2 dynamic
inline uint32_t automatic_multithreaded_dynamic(uint32_t number_of_points, const float* axis, int chunk_size, int threads) {
    threads = getThreads(threads);
    omp_set_num_threads(threads);

    vector<uint32_t> my_vector(threads, 0);
    #pragma omp parallel
    {
        MyXorshiftGen my_xorshift_gen(omp_get_thread_num(), axis);
        uint32_t count = 0;
        #pragma omp for schedule(dynamic, chunk_size)
        for (uint32_t i = 0; i < number_of_points; ++i) {
            if (hit_test(my_xorshift_gen.next_x(), my_xorshift_gen.next_y(), my_xorshift_gen.next_z())) {
                count += 1;
            }
        }
        my_vector[omp_get_thread_num()] = count;
    }
    return sum(my_vector, threads);
}

// Realisation 3 dynamic
inline uint32_t multithreaded_dynamic(uint32_t number_of_points, const float* axis, int threads, int chunk_size) {
    threads = getThreads(threads);
    omp_set_num_threads(threads);

    vector<uint32_t> my_vector(threads, 0);
    // for atomic operations
    atomic<uint32_t> atm_p(0);

    #pragma omp parallel
    {
        uint32_t count = 0;
        uint32_t p = 0;
        MyXorshiftGen my_xorshift_gen(omp_get_thread_num() + 123, axis);

        while (number_of_points > p) {
            while (true) {
                p = atm_p.load();
                if (atm_p.compare_exchange_weak(p, p + chunk_size)) {
                    break;
                }
            }

            if (number_of_points < p) {
                break;
            }

            for (uint32_t i = p; i < min(p + chunk_size, number_of_points); ++i) {
                if (hit_test(my_xorshift_gen.next_x(), my_xorshift_gen.next_y(), my_xorshift_gen.next_z())) {
                    count += 1;
                }
            }
        }
        my_vector[omp_get_thread_num()] = count;
    }

    return sum(my_vector, threads);
}

// Realisation 3 static
inline uint32_t multithreaded_static(uint32_t number_of_points, const float* axis, int threads, int chunk_size) {
    threads = getThreads(threads);
    omp_set_num_threads(threads);

    vector<uint32_t> my_vector(threads, 0);
    const uint32_t toUint32 = 0;
    const uint32_t step = threads * chunk_size;

    #pragma omp parallel
    {
        uint32_t thread_num = omp_get_thread_num();
        uint32_t p = thread_num * chunk_size;
        MyXorshiftGen my_xorshift_gen(thread_num, axis);

        uint32_t count = 0;
        while (p < number_of_points) {
            for (uint32_t i = 0; i < min(chunk_size + toUint32, number_of_points - p); ++i) {
                if (hit_test(my_xorshift_gen.next_x(), my_xorshift_gen.next_y(), my_xorshift_gen.next_z())) {
                    count += 1;
                }
            }
            p += step;
        }
        my_vector[thread_num] = count;
    }

    return sum(my_vector, threads);
}

// Exit from the program
void exitProgram(const string &message, const int exit_code) {
    cerr << message << endl;
    exit(exit_code);
}

// check realization
bool isValueRealizationCorrect(const string &realization) {
    if (realization == "1" || realization == "2" || realization == "3") {
        return true;
    }
    return false;
}

// checking for a number
bool isItNumber(const string &number) {
    for (int i = 0; i < number.length(); ++i) {
        if (!isdigit(number[i])) {
            return false;
        }
    }
    return true;
}

// check threads
bool isValueThreadsCorrect(const string &threads) {
    if (isItNumber(threads) && stoi(threads) >= 0) {
        return true;
    }
    return false;
}

// check kind
bool isValueKindCorrect(const string &kind) {
    if (kind == "static" || kind == "dynamic") {
        return true;
    }
    return false;
}

// read a number from a file
uint32_t readFile(const string &inpFile) {
    ifstream in(inpFile);
    if (!in.is_open()) {
        exitProgram("Couldn't open the file (read)", 1);
    }

    uint32_t number_of_points = 0;
    in >> number_of_points;
    in.close();
    return number_of_points;
}

// write a number to a file
void writeFile(const string &outFile, float answer) {
    ofstream out(outFile);
    if (!out.is_open()) {
        exitProgram("Couldn't open the file (write)", 1);
    }

    out << answer << "\n";
    out.close();
}

// calculate the amount of space
uint32_t getAmountOfSpace(const float* axis) {
    float amount_of_space = (axis[5] - axis[4]) * (axis[3] - axis[2]) * (axis[1] - axis[0]);
    if (amount_of_space <= 0) {
        exitProgram("Incorrect volume", 1);
    }
    return amount_of_space;
}

int main(int argc, char* argv[]) {
    const float* axis = get_axis_range();

    string inpFile, outFile;
    int realization = 2;
    int threads = -1;
    string kind = "dynamic";
    int chunk_size = 1024;

    // we get the basic settings and check them for correctness
    for (int i = 2; i < argc; i+=2) {
        string word = argv[i - 1];
        if (word == "--input") {
            inpFile = argv[i];
        } else if (word == "--output") {
            outFile = argv[i];
        } else if (word == "--realization") {
            if (isValueRealizationCorrect(argv[i])) {
                realization = stoi(argv[i]);
            } else {
                exitProgram("Incorrect realization value",  1);
            }
        } else if (word == "--threads") {
            if (isValueThreadsCorrect(argv[i])) {
                threads = stoi(argv[i]);
            } else {
                exitProgram("Incorrect threads value", 1);
            }
        } else if (word == "--kind") {
            if (isValueKindCorrect(argv[i])) {
                kind = argv[i];
            } else {
                exitProgram("Incorrect kind value", 1);
            }
        } else if (word == "--chunk_size") {
            if (isItNumber(argv[i])) {
                chunk_size = stoi(argv[i]);
            } else {
                exitProgram("Incorrect chunk_size value", 1);
            }
        }
    }

    // checking if there are file names
    if (inpFile.empty() || outFile.empty()) {
        exitProgram("Incorrect input/output file", 1);
    }

    // We get the number of points
    uint32_t number_of_points = readFile(inpFile);


    // We count the number of points that fall into the shape area
    uint32_t answer_hit = 0;
    // and we measure the time
    double timesStart = omp_get_wtime();
    if (realization == 1) {
        answer_hit = single_threaded_implementation(number_of_points, axis);
    } else if (realization == 2) {
        if (kind == "static") {
            answer_hit = automatic_multithreaded_static(number_of_points, axis, chunk_size, threads);
        } else if (kind == "dynamic") {
            answer_hit = automatic_multithreaded_dynamic(number_of_points, axis, chunk_size, threads);
        }
    } else if (realization == 3) {
        if (kind == "static") {
            answer_hit = multithreaded_static(number_of_points, axis, threads, chunk_size);
        } else if (kind == "dynamic") {
            answer_hit = multithreaded_dynamic(number_of_points, axis, threads, chunk_size);
        }
    }
    double timesEnd = omp_get_wtime();

    // calculating the wallpaper space
    float amount_of_space = getAmountOfSpace(axis);

    // calculating the volume of the shape
    float answer_volume = amount_of_space * (static_cast<float>(answer_hit) / static_cast<float>(number_of_points));

    // Writing the response to a file
    writeFile(outFile, answer_volume);

    // We output the response to the console
    if (realization == 2 || realization == 3) {
        printf("Time (%i thread(s)): %g ms\n", threads, (timesEnd - timesStart) * 1000);
    } else {
        printf("Time (%i thread(s)): %g ms\n", 0, (timesEnd - timesStart) * 1000);
    }
}