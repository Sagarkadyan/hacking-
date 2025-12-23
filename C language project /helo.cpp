#include <iostream>
#include <iomanip>

int main() {
    std::cout << "Calculator App" << std::endl;

    // Get input from the user
    double num1;
    std::cin >> num1;
    double num2;
    std::cin >> num2;

    // Print the numbers
    std::cout << "First number: " << num1 << std::endl;
    std::cout << "Second number: " << num2 << std::endl;
    std::cout << "Sum: " << std::fixed << std::setprecision(2) << num1 + num2 << std::endl;
    std::cout << "Difference: " << std::fixed << std::setprecision(2) << num1 - num2 << std::endl;
    std::cout << "Product: " << std::fixed << std::setprecision(2) << num1 * num2 << std::endl;
    std::cout << "Division: " << std::fixed << std::setprecision(2) << num1 / num2 << std::endl;

    return 0;
}