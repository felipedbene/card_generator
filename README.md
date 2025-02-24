# 🃏 AI Card Generator

This project is a 🏗️ card generator that allows you to create custom cards for various purposes. The main goal is to use the generated images as assets in a 🎮 game being developed. Another 🔥 Bedrock-powered tool!

## ⚙️ Installation

1️⃣ **Clone** the 📂 repository:
    ```bash
    git clone https://github.com/felipedbene/card_generator.git
    ```
2️⃣ **Navigate** to the project 📂 directory:
    ```bash
    cd card_generator
    ```
3️⃣ **Install** the required 📦 dependencies:
    ```bash
    uv install
    ```

4️⃣ **Create** a 🏗️ virtual environment:
    ```bash
    uv venv init
    ```

5️⃣ **Activate** the 🏗️ virtual environment:
    ```bash
    source .venv/bin/activate
    ```

6️⃣ **Install** the project 📦 dependencies:
    ```bash
    uv pip install -r requirements.txt
    ```

## 🚀 Usage

1️⃣ **Run** the 🃏 card generator script:
    ```bash
    python card_generator.py
    ```
2️⃣ The script will generate a **full tarot deck** 🃏 based on the predefined deck 📜 structure, ensuring accurate 🎭 symbolism and consistency with traditional 🔮 tarot readings.

3️⃣ The generated 🖼️ cards will be saved in a ⏳ timestamped 📂 directory under `tarot_images/`, following the format:
    ```
    tarot_images/tarot_run-YYYYMMDD-HHMMSS/
    ```
    Each 📂 file will be named according to the 🃏 card title, e.g., `the_fool.png`, `the_magician.png`.

4️⃣ You have to configure an ☁️ S3 bucket by modifying the `S3_BUCKET` variable inside `card_generator.py`.

## 🎯 Expected Results

After running the script, you should find a **complete 78-card** 🔮 tarot deck in the corresponding ⏳ timestamped 📂 directory within `tarot_images/`. The generated deck will closely resemble the reference 🔍 tarot structure in both **composition and 🎭 symbolic accuracy**.

Each 🃏 card is generated with:
- 📜 **Predefined descriptions** ensuring accurate 🖼️ representation.
- 🎭 **Symbolism** matching traditional 🔮 tarot interpretations.
- 🎨 **Consistent framing and design** across all 🃏 cards.

## 🤝 Contributing

1️⃣ **Fork** the 📂 repository.
2️⃣ **Create** a new 🌿 branch:
    ```bash
    git checkout -b feature-branch
    ```
3️⃣ **Make changes** and 💾 commit them:
    ```bash
    git commit -m "Description of changes"
    ```
4️⃣ **Push** to the 🌿 branch:
    ```bash
    git push origin feature-branch
    ```
5️⃣ **Create** a 🔀 pull request.

## 🛡️ License

This project is licensed under the 📝 MIT License. See the [LICENSE](LICENSE) file for details.

