Here’s the **updated README** with **instructions on how to use the `pyproject.toml` file with `uv`**:

```md
# 🃏 AI Card Generator

This project is a 🏗️ card generator that allows you to create custom cards for various purposes. The main goal is to use the generated images as assets in a 🎮 game being developed. Another 🔥 Bedrock-powered tool!

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/felipedbene/card_generator.git
```

### 2️⃣ Navigate to the Project Directory
```bash
cd card_generator
```

### 3️⃣ Install Dependencies with `uv`
The project uses `uv` for managing dependencies efficiently. To install all required dependencies, run:
```bash
uv pip install
```
This will automatically install the dependencies specified in `pyproject.toml`.

Alternatively, if you need to update dependencies later, you can run:
```bash
uv pip install --upgrade
```

### 4️⃣ Create & Activate a Virtual Environment
To keep dependencies isolated, create and activate a virtual environment:

```bash
uv venv init
source .venv/bin/activate
```

## 🚀 Usage

### 1️⃣ Run the 🃏 Card Generator Script
```bash
python card_generator.py
```

### 2️⃣ What Happens?
- The script generates a **full tarot deck** 🃏 based on the predefined deck 📜 structure.
- Ensures accurate 🎭 symbolism and consistency with traditional 🔮 tarot readings.
- Saves generated 🖼️ cards in a **timestamped directory** under `tarot_images/`:
    ```
    tarot_images/tarot_run-YYYYMMDD-HHMMSS/
    ```
- Each 📂 file is named according to the 🃏 card title, e.g., `the_fool.png`, `the_magician.png`.

## 🎯 Expected Results

After running the script, you should find a **complete 78-card** 🔮 tarot deck in the corresponding ⏳ timestamped 📂 directory within `tarot_images/`. The generated deck closely resembles the **traditional tarot structure** in terms of **composition and symbolic accuracy**.

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
```

---

### 🔧 **What's Updated?**
✅ **Clear instructions** on using `pyproject.toml` with `uv`.  
✅ **Simplified dependency management** with `uv pip install`.  
✅ **Step-by-step installation and usage flow.**  
✅ **Formatting fixes** for better readability.  

This should now **work seamlessly** with your setup! Let me know if you need **further tweaks**. 🚀