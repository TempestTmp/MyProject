#ifndef MYXORSHIFTGEN_H
#define MYXORSHIFTGEN_H
#include <cstdint>
#include <limits>

// A pseudorandom number generator based on the Xorshift algorithm
class MyXorshiftGen {
private:
    uint32_t step;
    const float min_x;
    const float max_x;
    const float min_y;
    const float max_y;
    const float min_z;
    const float max_z;

    // Generating a new step
    inline void generate(int i) {
        step ^= (step + i) << 13;
        step ^= (step + i) >> 17;
        step ^= (step + i) << 5;
    }

    // Entering a random number in the range [min_value:max_value]
    inline float calculate(const float min_value, const float max_value) {
        return min_value + (max_value - min_value) * (static_cast<float>(step) / std::numeric_limits<uint32_t>::max());
    }

public:
    explicit MyXorshiftGen(uint32_t seed, const float* axises) : step(seed),
        min_x(axises[0]), max_x(axises[1]), min_y(axises[2]), max_y(axises[3]), min_z(axises[4]), max_z(axises[5]) {}

    inline float next_x() {
        generate(1);
        return calculate(min_x, max_x);
    }
    inline float next_y() {
        generate(2);
        return calculate(min_y, max_y);
    }
    inline float next_z() {
        generate(3);
        return calculate(min_z, max_z);
    }
};

#endif //MYXORSHIFTGEN_H
