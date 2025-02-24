# Card Generator

This project is a card generator that allows you to create custom cards for various purposes.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/felipedbene/card_generator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd card_generator
    ```
3. Install the required dependencies:
    ```bash
    uv install
    ```

4. Create a virtual environment:
    ```bash
    uv venv init
    ```

5. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```

6. Install the project dependencies:
    ```bash
    uv pip install -r requirements.txt
    ```

## Usage

1. Run the card generator script:
    ```bash
    python card_generator.py
    ```
2. Follow the prompts to customize your card:
    - Enter the card title
    - Enter the card description
    - Choose a template
    - Customize the literals

3. The generated card will be saved in the `output` directory with a filename based on the card title.

## Expected Results

After running the script, you should find a new card file in the `output` directory. The card will be customized based on the inputs you provided.

## Contributing

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Description of changes"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
## License

This project is licensed under the BSD 3-Clause License. See the [LICENSE](LICENSE) file for details.