package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

// Reminder struct
type Reminder struct {
	Message string
	Delay   time.Duration
}

// Function to set a reminder
func (r Reminder) SetReminder() {
	fmt.Printf("Reminder set: '%s' in %v seconds\n", r.Message, r.Delay.Seconds())
	for i := int(r.Delay.Seconds()); i > 0; i-- {
		fmt.Printf("Time remaining: %d seconds\r", i)
		time.Sleep(1 * time.Second)
	}
	fmt.Println("\nReminder: ", r.Message)
}

func parseDuration(input string) (time.Duration, error) {
	input = strings.TrimSpace(input)
	if strings.HasSuffix(input, "m") {
		minutes, err := strconv.Atoi(strings.TrimSuffix(input, "m"))
		if err != nil {
			return 0, err
		}
		return time.Duration(minutes) * time.Minute, nil
	} else if strings.HasSuffix(input, "s") {
		seconds, err := strconv.Atoi(strings.TrimSuffix(input, "s"))
		if err != nil {
			return 0, err
		}
		return time.Duration(seconds) * time.Second, nil
	}
	return 0, fmt.Errorf("invalid format, use 'Xm' for minutes or 'Xs' for seconds")
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Println("Welcome to Kynefully Baked Reminder App!")
	fmt.Print("Enter your reminder message: ")
	message, _ := reader.ReadString('\n')
	message = strings.TrimSpace(message)

	fmt.Print("Enter delay time (e.g., 30s for seconds, 2m for minutes): ")
	delayInput, _ := reader.ReadString('\n')
	delayInput = strings.TrimSpace(delayInput)

	delay, err := parseDuration(delayInput)
	if err != nil {
		fmt.Println("Invalid input. Please use 'Xs' for seconds or 'Xm' for minutes.")
		return
	}

	reminder := Reminder{Message: message, Delay: delay}
	reminder.SetReminder()
}
