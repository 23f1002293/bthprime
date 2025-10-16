# P-th Prime Finder

## Summary

This is a minimal, working application that finds and displays the *p*-th prime number. It consists of two standalone components:

1.  A Python script (`main.py`) that can be run from the command line.
2.  An HTML file (`index.html`) with an interactive web interface that performs the calculation in-browser using JavaScript.

## Setup

No special setup is required as the project has no external dependencies.

### Prerequisites

-   Python 3.x (for running the command-line script)
-   A modern web browser (for the web interface)

### Installation

Simply download or clone the repository files.

```bash
git clone <repository-url>
cd <repository-directory>
```

## Usage

### Command-Line Interface

You can run the Python script from your terminal to find the *p*-th prime.

**Syntax:**

```bash
python main.py <p>
```

Where `<p>` is a positive integer.

**Examples:**

```bash
# Find the 1st prime
$ python main.py 1
The 1th prime number is: 2

# Find the 10th prime
$ python main.py 10
The 10th prime number is: 29

# Find the 10,001st prime
$ python main.py 10001
The 10001th prime number is: 104743
```

### Web Interface

Open the `index.html` file in your web browser.

1.  Enter a positive integer in the input field.
2.  Click the "Find Prime" button.
3.  The result will be displayed below the button.

**Note:** Calculating very large primes (e.g., the 100,000th) can take a few seconds and may cause the browser to become unresponsive temporarily.

## Code Explanation

### `main.py`

This script contains two main functions:

-   `is_prime(n)`: An efficient function that checks if a given number `n` is prime. It uses an optimized trial division method, checking for divisibility by 2 and 3, and then only checking numbers of the form `6k ± 1` up to the square root of `n`.
-   `get_pth_prime(p)`: This function iterates through numbers (starting from 2 and then only odd numbers), uses `is_prime` to check each one, and counts until it finds the *p*-th prime.

The script also includes a `main` block to handle command-line argument parsing and error handling.

### `index.html`

This is a single, self-contained HTML file.

-   **HTML:** Defines the basic structure of the page, including a title, a form with a number input and a submit button, and a paragraph element to display the result.
-   **CSS:** Minimal inline CSS is included within a `<style>` tag for basic layout and aesthetics.
-   **JavaScript:** The core logic is embedded in a `<script>` tag. The `is_prime` and `getPthPrime` functions are JavaScript implementations of the same logic found in the Python script. An event listener is attached to the form's `submit` event, which triggers the prime calculation and updates the DOM to display the result or any input errors.

## License

This project is licensed under the MIT License.
