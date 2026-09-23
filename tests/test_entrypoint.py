from platform.config.entrypoint import EntrypointLoader


def main():
    train_function = EntrypointLoader.load(
        "project.train:train"
    )

    print("Entrypoint loaded successfully.")
    print(f"Loaded function: {train_function}")


if __name__ == "__main__":
    main()