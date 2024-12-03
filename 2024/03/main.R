read_input <- function(input_file) {
  input_file |> readr::read_file()
}

mul <- function(a, b) {
  a * b
}

part1 <- function(input) {
  input |>
    stringr::str_extract_all(
      stringr::regex("mul\\([:digit:]+,[:digit:]+\\)")
    ) |>
    unlist() |>
    tibble::as_tibble_col(column_name = "expr_str") |>
    purrr::pmap(\(expr_str) str2expression(expr_str)) |>
    purrr::map(eval) |>
    unlist() |>
    sum() |>
    print()
}

part2 <- function(input) {
  do <- TRUE
  do_or_dont <- function(x) {
    if (x == "don't()") {
      do <<- FALSE
    } else if (x == "do()") {
      do <<- TRUE
    }
    do
  }

  input |>
    stringr::str_extract_all(
      stringr::regex("(mul\\([:digit:]+,[:digit:]+\\))|do\\(\\)|don't\\(\\)")
    ) |>
    unlist() |>
    tibble::as_tibble_col(column_name = "expr_str") |>
    dplyr::rowwise() |>
    dplyr::mutate(include = do_or_dont(expr_str)) |>
    dplyr::ungroup() |>
    dplyr::filter(include == TRUE, expr_str != "do()") |>
    dplyr::select(expr_str) |>
    purrr::pmap(\(expr_str) str2expression(expr_str)) |>
    purrr::map(eval) |>
    unlist() |>
    sum() |>
    print()
}

input_file <- "2024/03/input.txt"
input <- read_input(input_file)
part1(input)
part2(input)
