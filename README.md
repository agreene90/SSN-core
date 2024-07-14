# **SSN-Core: Sensor and Servo Network Core Framework**

## **Overview**
The **SSN-Core** framework provides a robust and flexible foundation for developing applications that involve sensor data processing, natural language understanding (NLU), text-to-speech (TTS) capabilities, and servo control. This framework is designed for developers looking to create complex systems with integrated sensor and servo operations, alongside advanced NLU and TTS functionalities.
__
![img](https://github.com/agreene90/SSN-core/blob/main/ssn-c.png)
___
## **Installation**
1. **Clone the repository:**
   ```sh
   git clone https://github.com/LoQiseaking69/SSN-core.git
   cd SSN-core
   ```

2. **Install required dependencies:**
   Ensure you have Python 3.8+ installed. Then, install the necessary Python packages:
   ```sh
   pip install -r requirements.txt
   ```

## **Usage**
1. **Configuration:**
   Configure the necessary settings in `core_framework.py`, `nlu_tts_modules.py`, and `servo_control_module.py` as per your application requirements.

2. **Running the application:**
   Execute the main script to start the application:
   ```sh
   python main.py
   ```

## **Files Description**
- **core_framework.py:** Contains the core functionalities and classes required for initializing and managing the sensor and servo network. This file is the backbone of the framework, ensuring smooth communication between different modules.
  
- **nlu_tts_modules.py:** Includes the modules responsible for natural language understanding and text-to-speech. This file contains methods for processing user input, understanding commands, and generating speech output.
  
- **servo_control_module.py:** Manages the control of servos. It provides functions to initialize servos, send control signals, and manage their states.

- **main.py:** The entry point of the application. This file integrates all modules and starts the execution of the framework.

## **License**
This project is licensed under the BSD 3-Clause License. See the LICENSE file for more details.

