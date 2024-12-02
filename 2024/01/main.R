read_input <- function(input_file) {
  input_file |>
    readr::read_delim(
      delim = "   ",
      col_names = c("A", "B"),
      col_types = "ii",
      progress = FALSE,
      show_col_types = FALSE
    )
}

part1 <- function(input) {
  input |>
    dplyr::select(A) |>
    dplyr::arrange(A) |>
    dplyr::bind_cols(
      input |>
        dplyr::select(B) |>
        dplyr::arrange(B)
    ) |>
    dplyr::mutate(diff = abs(B - A)) |>
    dplyr::pull(diff) |>
    sum() |>
    print()
}

part2 <- function(input) {
  input |>
    dplyr::select(A) |>
    dplyr::left_join(
      input |> dplyr::count(B),
      by = dplyr::join_by(A == B)
    ) |>
    dplyr::mutate(sim = A * n) |>
    dplyr::pull(sim) |>
    sum(na.rm = TRUE) |>
    print()
}

input_file <- "2024/01/input.txt"
input <- read_input(input_file)
part1(input)
part2(input)
