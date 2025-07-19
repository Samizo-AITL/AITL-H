#include <stdio.h>

double kp = 1.2, ki = 0.4, kd = 0.1;
double setpoint = 90;
double out_min = -100, out_max = 100;
double integral = 0, prev_error = 0;

double pid_step(double input) {
    double error = setpoint - input;
    integral += error;
    double derivative = error - prev_error;
    double output = kp * error + ki * integral + kd * derivative;
    if (output > out_max) output = out_max;
    if (output < out_min) output = out_min;
    prev_error = error;
    return output;
}
