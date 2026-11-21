import os

TEXT = "The tide left so quietly that nobody saw the harbour turn to glass; gulls walked out on it, and for one hour the whole town could hear the sea breathing underneath, patient, enormous, and entirely unbothered by us."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as output:
        output.write(TEXT)
    print(len(TEXT))


if __name__ == "__main__":
    main()
