task_text = ('''$dF-BY!tM=8-VBU-VOOdABME>8d-3B9hABh98-IY>>8$-AUBU98dU!d3QdLMEYCB-!83B98W-IU3BhQ-A-VtdKd>BYK
U>M-U3>UEY>8->Y-M3QUtGJUEY>MM-$dFOh>A=MM-AUBU9YPQ9dU!9YJhdB-AtCLM-E-M>IdA38-KY33MEY
U3>UE>8K-Q9dMKhnd3BEUK-$dF-BY!tM=-PEtPdB3P-M$-3QU3U!>U3BGU!d3QdLMEYBG-!83B98W-QUM3A-IU!YEtd>Md-M-hIYtd>Md-VtdKd>BUE
AtY338-$dF-BY!tM=-KURhB-9YJtMLYBG3P-QU-3QU3U!h-U!9Y!UBAMAUttMJMW-3MBhY=MW-AURIY-IEY-AtCLY-$dFM9hCB3P-E-UIM>-MBUB-Zd-M>IdA3
3hnd3BEhCB-IEY-U3>UE>8$-KdBUIY-=dQULdL>YP-YI9d3Y=MP-MUBA98BYP-YI9d3Y=MP
Q9M-=dQULdL>UW-YI9d3Y=MM-AYZI8W-VtdKd>B-KY33MEY-$9Y>MB338tAh->Y-3QM3UA-VtdKd>BUE-AUBU98d-MKdCB-UIM>YAUE8W-$dF
VBU-QUJEUtPdB-IU!YEtPBG->UE8d-VtdKd>B8-!dJ->dU!$UIMKU3BMQd9d9Y3Q9dIdtPBG-3hnd3BEhCnMd
UBA98BYP-YI9d3Y=MP-E-3EUC-ULd9dIG-B9d!hdB-QUM3AY-3tdIhCndRU3EU!UI>URU-M>IdA3Y-E-3thLYd-AUttMJMM-LBU-KUZdB-Q9MEd3BM-A3>MZd>MC-Q9UMJEUIMBdtG>U3BM-Q9M-E83UAUW-JYR9hJAdBY!tM=8
E8!U9-KdBUIY-JYEM3MB-UB-B9d!UEY>MW-A-!83B9UIdW3BEMC-MU!xdKh-IY>>8$
A9UKd-BURU-$dFBY!tM=8-KURhB-!8BG-IM>YKMLd3AMKM-LBUQUJEUtPdB-MJKd>PBG-M$-9YJKd9-E-Q9U=d33d-9Y!UB8-U!d3QdLMEYPBdK-3YK8K-UQBMKMJY=MC-QYKPBM-M-Q9UMJEUIMBdtG>U3BM''')

rus_freq: dict[str, float] = {
    'о': 0.0965, 'и': 0.0753, 'е': 0.0723, 'а': 0.0648, 'н': 0.0618,
    'т': 0.0616, 'с': 0.0520, 'р': 0.0407, 'в': 0.0393, 'м': 0.0298,
    'л': 0.0294, 'д': 0.0270, 'я': 0.0264, 'к': 0.0260, 'п': 0.0248,
    'з': 0.0160, 'ы': 0.0157, 'ь': 0.0151, 'у': 0.0133, 'ч': 0.0117,
    'ж': 0.0107, 'г': 0.0099, 'х': 0.0087, 'ф': 0.0073, 'й': 0.0069,
    'ю': 0.0067, 'б': 0.0067, 'ц': 0.0050, 'ш': 0.0042, 'щ': 0.0036,
    'э': 0.0024, 'ъ': 0.0004, 'ё': 0.0004, ' ': 0.1287
}


def write_to_file(filename: str, content: str) -> None:
    """
    Writes the given content to a file.

    :param filename: name of the file to write
    :param content: content to be written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def replace_chars(text: str, target_char: str, replacement_char: str) -> str:
    """
    Replaces all occurrences of target_char with replacement_char in the given text.

    :param text: the input text
    :param target_char: character to be replaced
    :param replacement_char: character to replace with
    :return: modified text with replacements
    """
    return text.replace(target_char, replacement_char)


def calculate_char_percentages(text: str) -> list[tuple[str, float]]:
    """
    Calculates the frequency percentage of each unique character in the text.

    :param text: the input text
    :return: list of tuples with character and its percentage, sorted descending
    """
    text_len = len(text)
    uniq_chars = set(text)
    char_percentages = {
        char: text.count(char) / text_len for char in uniq_chars
    }
    return sorted(char_percentages.items(), key=lambda item: item[1], reverse=True)


def main() -> None:
    text = task_text

    print("\nEncrypted text:\n")
    print(text)

    percent_dict = calculate_char_percentages(text)

    print("\n______________________________________________________________\n")
    print("Character frequency percentages in the encrypted text:\n")
    sorted_dict = {
        i: val for i, val in sorted(enumerate(percent_dict), key=lambda x: x[0])
    }
    print(sorted_dict)

    print("\nRussian frequency dictionary:\n")
    print(rus_freq)

    print("\n______________________________________________________________\n")
    print("Decrypted text:\n")

    replacements: dict[str, str] = {
        '-': ' ', 'U': 'о', 'B': 'т', 'V': 'э', 'd': 'е', 'R': 'г', 'A': 'к',
        '9': 'р', 'K': 'м', 'h': 'у', 'I': 'д', 'O': 'ф', 'M': 'и', 'E': 'в',
        '8': 'ы', '>': 'н', '3': 'с', 'Y': 'а', '$': 'х', 'F': 'ш', '!': 'б',
        'Q': 'п', 'L': 'ч', 'C': 'ю', 'W': 'й', 't': 'л', '=': 'ц', 'G': 'ь',
        'J': 'з', 'P': 'я', 'Z': 'ж', 'n': 'щ', 'x': 'ъ'
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    print(text)
    print("\n")


if __name__ == "__main__":
    main()
