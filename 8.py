from collections import namedtuple

Participant = namedtuple("Participant", "lastName firstName school score")


def main():
    with open("input8.txt", encoding='utf-8') as fin, open("output8.txt", "w") as fout:
        participants = [Participant(*i.split()) for i in fin]
        participants.sort(key=lambda x: x.lastName)
        print(*map(" ".join, participants), sep="\n", file=fout)


if __name__ == "__main__":
    main()
