import time
from data_analyzer import Dataanalyzer
from data_visualizer import DataVisualizer
from model_trainer import ModelTrainer


def run_pipeline():
    file_path = "students_200.csv"

    print("=" * 60)
    print("        STUDENT PERFORMANCE PREDICTION PIPELINE")
    print("=" * 60)
    time.sleep(1)

    print("\n[Step 1] Loading and Analyzing Dataset...")
    time.sleep(1)
    analyzer = Dataanalyzer(file_path)
    summary = analyzer.summary()
    print(f"Dataset Loaded: {summary['shapes'][0]} rows, {summary['shapes'][1]} columns")
    high_performers = analyzer.get_high_perfomers()
    print(f"High Performing Students Count: {len(high_performers)}")

    print("\n[Step 2] Generating Data Visualizations...")
    time.sleep(1)
    visualizer = DataVisualizer(file_path)

    print("  -> Creating Line Chart...")
    visualizer.plot_line_chart(show=True)
    time.sleep(0.5)

    print("  -> Creating Scatter Plot...")
    visualizer.plot_scatter_plot(show=True)
    time.sleep(0.5)

    print("  -> Creating Bar Chart...")
    visualizer.plot_bar_chart(show=True)
    time.sleep(0.5)

    print("  -> Creating Histogram...")
    visualizer.plot_histogram(show=True)
    time.sleep(0.5)

    print("All charts have been created and saved successfully.")

    print("\n[Step 3] Training Machine Learning Models...")
    time.sleep(1)
    features = ["Attendance", "StudyHours", "AssignmentScore", "InternalMarks", "PreviousGPA"]
    target = "FinalMarks"
    trainer = ModelTrainer(analyzer.df, features, target)

    print("  -> Training Linear Regression...")
    trainer.train_linear_regression()
    time.sleep(0.5)

    print("  -> Training Linear Regression with Grid Search...")
    trainer.train_linear_grid()
    time.sleep(0.5)

    print("  -> Training Linear Regression with Random Search...")
    trainer.train_linear_random_search()
    time.sleep(0.5)

    print("  -> Training Ridge Regression...")
    trainer.train_ridge_linear()
    time.sleep(0.5)

    print("  -> Training Ridge Regression with Grid Search...")
    trainer.train_ridge_grid()
    time.sleep(0.5)

    print("\nModel Evaluation Metrics:")
    for name, metrics in trainer.model_metrics.items():
        print(f"  {name:22} | MAE: {metrics['MAE']:.3f} | RMSE: {metrics['RMSE']:.3f} | R2: {metrics['R2']:.3f}")

    print("\n[Step 4] Making Predictions for Sample Student...")
    time.sleep(1)
    sample_student = {
        "Attendance": 85.0,
        "StudyHours": 6.0,
        "AssignmentScore": 75.0,
        "InternalMarks": 80.0,
        "PreviousGPA": 8.5
    }
    print("Input Student Profile:")
    for feature, value in sample_student.items():
        print(f"  {feature}: {value}")

    predicted_marks = trainer.predict_studentmarks(sample_student)
    print(f"\nPredicted Final Marks: {predicted_marks:.2f}")

    time.sleep(1)
    print("\n" + "=" * 60)
    print("        Pipeline Execution Completed Successfully!")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()
