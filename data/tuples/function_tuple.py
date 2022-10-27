def liklihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


def main():
    _likelihoods = liklihood()
    print(f"Minimum likelihood of falling: {_likelihoods[0]}%")
    print(f"Minimum likelihood of falling: {_likelihoods[1]}%")


if __name__ == "__main__":
    main()
