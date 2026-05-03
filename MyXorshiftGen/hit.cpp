#include "hit.h"

const float a = 2.0f;

// We check whether the point falls into the space of our figure
bool hit_test(float x, float y, float z)
{
    float x_2 = x * x;
    float x_4 = x_2 * x_2;
    float x_3 = x_2 * x;
    // the drop formula
    float formula = x_4 - a * x_3  + (a * a) * (y * y + z * z);
    return formula <= 0;

}

// creating the vertices of the cube
static const float axis[6] = {
    -a, a, // min_x, max_x
    -a, a, // min_y, max_y
    -a, a // min_z, max_z
};

// gives axis
const float* get_axis_range()
{
    return axis;
}
