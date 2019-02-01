from polyaxon_client.tracking import Experiment


def main():
    experiment = Experiment()
    print("Hello, World!")
    dummy_accuracy = 0.99
    experiment.log_metrics(accuracy=dummy_accuracy)


if __name__ == '__main__':
    main()
