![Goriber Tesla Demo](https://i.ibb.co.com/BH0tKgTS/image.png)

# 🚗 Goriber Tesla

---

Goriber Tesla is a fun mini-project built with **Python** and **Pygame**, where a car automatically drives on a predefined track using pixel color detection logic.

---

## 🎮 Features

-   Self-driving car simulation
-   Uses virtual camera logic to detect track path
-   Directional control with automatic turning
-   Smooth movement at 60 FPS
-   Track and car images loaded dynamically

---

## 🧠 How It Works

-   A virtual camera checks pixel colors in front of the car.
-   If the car detects a white pixel (`RGB(255,255,255)`), it continues moving in that direction.
-   When it detects a turn (black pixel ahead but white on the side), it changes direction and rotates the car image accordingly.

---

## ▶️ How to Run

1. Install Pygame (if not already):
    ```bash
    pip install pygame
    ```
