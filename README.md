# Petrol Price Intelligence Pipeline - Phase 1

This is the first phase of the Petrol Price Intelligence Pipeline project. The objective is to automate the retrieval of petrol price data, store it, and monitor the data regularly using Apache Airflow.

## 🚀 Project Setup

1. **Clone this repository**:
    ```bash
    git clone https://github.com/yourusername/petrol-price-intelligence.git
    cd petrol-price-intelligence
    ```

2. **Install dependencies**:
    You can install the required dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

3. **Start Airflow**:
    Make sure Docker is running and execute the following command to start all Airflow services:
    ```bash
    docker-compose up
    ```

4. **Access Airflow UI**:
    Go to the Airflow Web UI at [http://localhost:8080](http://localhost:8080) and log in with the default credentials:
    - **Username**: `airflow`
    - **Password**: `airflow`

5. **Trigger the DAG**:
    In the Airflow UI, **turn on** the DAG `petrol_price_pipeline_v1` and **trigger it manually**.

6. **Check the logs** for the **start and end messages**.

## 🛠 **Code Walkthrough**

In **Phase 1**, we create a simple DAG that:
- Runs daily at **7 AM**.
- Prints **"Petrol Price Pipeline Started"** and **"Pipeline Completed"**.

This DAG serves as the foundation for future steps where we’ll extract, transform, and load petrol price data.

## 📁 Directory Structure

- `dags/`: Contains Airflow DAGs.
- `logs/`: Logs are automatically created by Airflow.
- `data/`: Stores any sample data used in the project (e.g., petrol price data).
- `screenshots/`: Contains screenshots of the Airflow UI.
- `README.md`: Project documentation.

## 📝 **Phase 2 (Next Steps)**

In **Phase 2**, we’ll be **fetching petrol price data** from the API (or using dummy data for now) and begin processing it.

## 🧑‍💻 **Contributions**

Feel free to fork the repository and create a pull request with improvements or additional features.
