import pandas as pd


def analyze_bug_detection(file_name):
    df = pd.read_csv(file_name)

    # Identify missed bugs
    df["bug_missed"] = (
        df["expected_bug"] != df["detected_bug"]
    )

    # Identify incorrect suggestions
    df["incorrect_suggestion"] = (
        df["correct_suggestion"] == False
    )

    missed_bugs = df[df["bug_missed"] == True]

    incorrect_suggestions = df[
        df["incorrect_suggestion"] == True
    ]

    # Calculate metrics
    total_cases = len(df)

    correctly_detected = len(
        df[df["expected_bug"] == df["detected_bug"]]
    )

    correct_suggestions = len(
        df[df["correct_suggestion"] == True]
    )

    detection_rate = (
        correctly_detected / total_cases
    ) * 100

    suggestion_accuracy = (
        correct_suggestions / total_cases
    ) * 100

    overall_score = (
        detection_rate * 0.5
        + suggestion_accuracy * 0.5
    )

    # Performance level
    if overall_score >= 90:
        performance = "Excellent"
    elif overall_score >= 75:
        performance = "Good"
    elif overall_score >= 60:
        performance = "Moderate"
    else:
        performance = "Needs Improvement"

    # Display results
    print("=" * 70)
    print("                    BUGGAP ANALYZER")
    print("=" * 70)

    print("\nFINAL RESULTS")
    print("-" * 70)

    print(f"Bug Detection Rate     : {detection_rate:.2f}%")
    print(f"Suggestion Accuracy    : {suggestion_accuracy:.2f}%")
    print(f"Missed Bugs            : {len(missed_bugs)}")
    print(
        f"Incorrect Suggestions  : "
        f"{len(incorrect_suggestions)}"
    )
    print(f"Overall Score          : {overall_score:.2f}%")
    print(f"Performance            : {performance}")

    print("\n" + "-" * 70)
    print("MISSED BUGS")
    print("-" * 70)

    for _, row in missed_bugs.iterrows():
        print(f"\nTest Case : {row['test_case']}")
        print(f"Expected  : {row['expected_bug']}")
        print(f"Detected  : {row['detected_bug']}")

    print("\n" + "-" * 70)
    print("INCORRECT SUGGESTIONS")
    print("-" * 70)

    for _, row in incorrect_suggestions.iterrows():
        print(f"\nTest Case   : {row['test_case']}")
        print(f"Expected Bug: {row['expected_bug']}")
        print(f"Suggestion  : {row['suggestion']}")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    analyze_bug_detection("bug_evaluation_dataset.csv")