#include "ros/ros.h"
#include "sensor_msgs/Joy.h"
#include <iostream>
#include <thread>
#include <chrono>

// You may need to adjust these values based on your system and preferences
#define NOTE_C4 261.63
#define NOTE_D4 293.66
#define NOTE_E4 329.63
#define NOTE_F4 349.23
#define NOTE_G4 392.00
#define NOTE_A4 440.00
#define NOTE_B4 493.88
#define NOTE_C5 523.25
#define NOTE_REST 0

class MelodyNode {
public:
    MelodyNode() : nh_(), joy_subscriber_(nh_.subscribe("joy", 10, &MelodyNode::joyCallback, this)) {
        // Initialize any variables or setup you need here
    }

    void joyCallback(const sensor_msgs::Joy::ConstPtr& joy_msg) {
        // Extract button state from the Joy message
        // bool button_pressed = joy_msg->buttons[0]; // Assuming the first button is used to trigger the melody

        // // If the button is pressed, play the melody
        // if (button_pressed) {
        //     playMelody();
        // }
    }

    void playMelody() {
        // Define your melody sequence here
        // double melody[] = {NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5, NOTE_REST};
        // int noteDuration = 500; // in milliseconds

        // for (int i = 0; i < sizeof(melody) / sizeof(*melody); ++i) {
        //     if (melody[i] == NOTE_REST) {
        //         // Pause if the note is a rest
        //         std::this_thread::sleep_for(noteDuration);
        //     } else {
        //         // Play the note
        //         tone(8, melody[i], noteDuration);
        //         std::this_thread::sleep_for(noteDuration * 1.1); // Wait for the note to finish
        //     }
        // }
    }

private:
    ros::NodeHandle nh_;
    ros::Subscriber joy_subscriber_;
};

int main(int argc, char **argv) {
    ros::init(argc, argv, "melody_node");
    MelodyNode node;
    ros::spin();
    return 0;
}