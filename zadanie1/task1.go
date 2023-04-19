package main

import "fmt"

func main() {
	robot1position := 1
	total := 0
	robot2position := 100
	start1 := robot1position
	start2 := robot2position
	blackpoint := 52
	for IfFlag(robot2position, blackpoint) == false {
		MoveLeft(robot2position)
		MoveLeft(robot1position)
		robot1position -= 1
		robot2position -= 1
		if robot2position == start1 {
			MoveLeft(robot2position)
			robot2position -= 1
		} else {
			MoveLeft(robot2position)
			robot2position -= 1
			total += 1
		}
		if robot1position == start2 {
			MoveLeft(robot1position)
			robot1position -= 1
			fmt.Println(robot1position)
		} else {
			MoveLeft(robot1position)
			robot1position -= 1
			total += 1
		}
	}
	fmt.Println("Программа выполнилась за", total, "сек.")

}
func MoveLeft(robotposition int) {
	robotposition -= 1

}
func MoveRight(robotposition int) {
	robotposition += 1
	fmt.Println(robotposition)
}
func IfFlag(robotposition, blackpoint int) bool {
	if robotposition == blackpoint {
		fmt.Println("Роботы встретились на клетке с номером", blackpoint)
		return true
	}
	return false
}
