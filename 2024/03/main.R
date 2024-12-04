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
    dplyr::mutate(
      expr = purrr::map(expr_str, str2expression),
      res = unlist(purrr::map(expr, eval))
    ) |>
    dplyr::pull(res) |>
    sum()
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
    sum(na.rm = TRUE)
}

argv <- argparser::arg_parser(
  name = "main.R",
  description = paste(
    # UPDATE DAY
    "Advent of Code 2024, Day 3:",
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
