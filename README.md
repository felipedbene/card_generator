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
    ```bash# Card Generator

This project is a tarot card generator that uses AI to create a full deck of tarot cards while ensuring accurate symbolism. The generated images are saved locally, and users can configure S3 storage if needed.

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
2. The script will generate a **full tarot deck** based on the predefined deck structure, ensuring accurate symbolism and consistency with traditional tarot readings.

3. The generated cards will be saved in a timestamped directory under `tarot_images/`, following the format:
    ```
    tarot_images/tarot_run-YYYYMMDD-HHMMSS/
    ```
    Each file will be named according to the card title, e.g., `the_fool.png`, `the_magician.png`.

4. If desired, you can configure an S3 bucket by modifying the `S3_BUCKET` variable inside `card_generator.py`.

## Expected Results

After running the script, you should find a **complete 78-card tarot deck** in the corresponding timestamped directory within `tarot_images/`. The generated deck will closely resemble the reference tarot structure in both **composition and symbolic accuracy**.

Each card is generated with:
- **Predefined descriptions** ensuring accurate representation.
- **Symbolism matching traditional tarot interpretations.**
- **Consistent framing and design across all cards.**

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