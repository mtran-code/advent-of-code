#!/usr/bin/env -S Rscript --vanilla

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
    sum()
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
    sum()
}

argv <- argparser::arg_parser(
  name = "main.R",
  description = paste(
    # UPDATE DAY
    "Advent of Code 2024, Day X:",
    "Take input file containing raw text input, and",
    "print out solution to either part 1 or part 2."
  ),
  hide.opts = TRUE
) |>
  argparser::add_argument(
    arg = "input", help = "Input text file path."
  ) |>
  argparser::add_argument(
    arg = "part", help = "Which part to solve, either 1 or 2.",
    type = "integer"
  ) |>
  argparser::parse_args()

input <- argv$input |>
  read_input()

argv$part |>
  switch(input |> part1() |> cat(sep = "\n"),
    input |> part2() |> cat(sep = "\n")
  )
