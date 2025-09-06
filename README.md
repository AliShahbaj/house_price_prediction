# 🏠 House Price Prediction (Flask + Machine Learning)

A simple machine learning + Flask web app that predicts house prices based on size (square feet).
This project demonstrates how to **train a model in Python** and then **deploy it with Flask** as a web app.

---

## 📂 Project Structure
```
house_price_prediction/
│── train_model.py        # Script to train and save the model
│── app.py                # Flask web application
│── house_price_model.pkl # Saved ML model
│── templates/
│   └── index.html        # Frontend HTML form
│── README.md             # Project documentation
```

---

## ⚙️ Installation & Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

1. Clone the repo:
   ```bash
   git clone https://github.com/AliShahbaj/house_price_prediction.git
   cd house_price_prediction
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Train the model:
   ```bash
   uv run train_model.py
   ```

4. Run the Flask app:
   ```bash
   uv run app.py
   ```

---

## 🌐 Usage
1. Open the app in your browser:  
   👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

2. Enter a house size (e.g., `1800` sq ft).

3. Get a predicted price instantly 🎉

---

## 📊 Example
For a house of **1800 sq ft**, the model predicts:

```
Predicted House Price: ₹ 360000.0
```

---

## 🔧 Tech Stack
- **Python** (pandas, scikit-learn, pickle)
- **Flask** (for serving the model as a web app)
- **HTML** (basic frontend form)
- **uv** (dependency & environment manager)

---

## 🚀 Future Improvements
- Add more features (location, bedrooms, bathrooms, etc.)
- Use real datasets instead of sample data
- Improve frontend with CSS/Bootstrap
- Deploy on Render / Vercel / Heroku

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
