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
    dplyr::mutate(
      expr = purrr::map(expr_str, str2expression),
      res = unlist(purrr::map(expr, eval))
    ) |>
    dplyr::pull(res) |>
    sum() |>
    print()
}

part2 <- function(input) {
  multiplier <- 1
  do <- function() {
    multiplier <<- 1
    NA
  }
  dont <- function() {
    multiplier <<- 0
    NA
  }
  eval_dos <- function(expr) {
    eval(expr) * multiplier
  }

  input |>
    stringr::str_extract_all(
      stringr::regex("(mul\\([:digit:]+,[:digit:]+\\))|do\\(\\)|don't\\(\\)")
    ) |>
    unlist() |>
    tibble::as_tibble_col(column_name = "expr_str") |>
    dplyr::mutate(
      expr_str = purrr::modify_if(expr_str, \(x) x == "don't()", ~"dont()"),
      expr = purrr::map(expr_str, str2expression),
      res = unlist(purrr::map(expr, eval_dos))
    ) |>
    dplyr::pull(res) |>
    sum(na.rm = TRUE) |>
    print()
}

input_file <- "2024/03/input.txt"
input <- read_input(input_file)
part1(input)
part2(input)
