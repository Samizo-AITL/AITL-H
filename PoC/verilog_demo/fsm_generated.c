#include <stdio.h>
#include <string.h>

typedef enum {
    STATE_IDLE,
    STATE_TRACK,
    STATE_RECOVERY
} FSMState;

FSMState state = STATE_IDLE;

void fsm_step(const char* input) {
    switch (state) {
        case STATE_IDLE:
            if (strcmp(input, "start_signal") == 0) state = STATE_TRACK;
            break;
        case STATE_TRACK:
            if (strcmp(input, "lost_target") == 0) state = STATE_RECOVERY;
            break;
        case STATE_RECOVERY:
            if (strcmp(input, "recovered") == 0) state = STATE_IDLE;
            break;
    }
}
