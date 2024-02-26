<style>
.thin{
width:70px;
max-width:70px;
}
.desc{
width: 200px;
max-width: 200px;
}
.prereq{
width: 200px;
max-width: 200px;
}
.steps{
width: 300px;
max-width: 300px;
}
.exres{
width: 450px;
max-width: 450px;
}
.acres{
width: 200px;
max-width: 200px;
}
}
</style>

| <div class="thin">Test case ID </div> | <div class="desc">Test case description </div>| <div class="prereq">Prerequisites </div> | <div class="steps"> Test steps </div>| <div class="exres">Expected Result </div>| <div class="acres">Actual Result </div> | <div class="thin">Status </div> | <div class="thin">Created By </div> | <div class="thin"> Date of creation </div>|  <div class="thin"> Executed By </div> | <div class="thin"> Date of execution </div> |
|--|--|--|--|--|--|--|--|--|--|--|
| qpdTC001 | The objective of this test case is to verify this program functionality with valid input. | A valid input consists of a single integer. | 1. Run the program. <br> 2. Upon receiving an input prompt enter the number 222. <br> 3. Continue entering integers on each input prompt, e.g. 4, 6, 60, -42, -13. <br> 4. Enter 0 to get the program's output and terminate its execution. | 1. An input prompt appears on the screen with the text: “Enter an integer number:” <br> 2. A new input prompt with the following message “Enter an integer number:” appears on the line below the latest input. <br> 3. The program shall not give any error messages and shall continue to operate as usual upon receiving each of these inputs.s <br> 4. The program presents the user with the largest sum of digits (6) from the input sequence and list all numbers with this maximum sum of digits (222, 6, 60, -42).| 1.-4. The expected result has been received and thus functionality of the program has been confirmed.| <div style="color:#00cc00">Succes </div>| Sergo3682 | 26/02/2024 | Sergo3682 | 26/02/2024 |
| qpdTC002 | The objective of this test case is to verify that the program can process invalid input and give a corresponding warning message. | A valid input consists of digits and if needed “-” as the first character in line indicating a negative value. There should be no spaces before or between the characters representing the input integer. | 1. Run the program. <br> 2. Upon receiving an input prompt enter the following character sequence: “HelloWorld”. <br> 3. Upon receiving an input prompt enter the number 12.5. <br> 4. Upon receiving an input prompt enter the following character sequence: «./21*^7$4;». <br> 5. Enter 0 to get the program's output and terminate its execution. | 1. An input prompt appears on the screen with the text: “Enter an integer number:” <br> 2.-4. When the invalid input has been received the program shall notify the user about it with the following warning message: “Invalid input. Please try again.” Then the program shall proceed to display the next input prompt. <br> 5. The program presents the user with the largest sum of digits (0) from the input sequence and list all numbers with this maximum sum of digits (0). | 1.-5. The expected result has been confirmed. | <div style="color:#00cc00"> Succes </div> | Sergo3682 | 26/02/2024 | Sergo3682 | 26/02/2024 |
| qpdTC003 | The objective of this test case is to verify this program functionality with no input. |  |  |  |  |  |  |  |  |  | 
