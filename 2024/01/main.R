#!/usr/bin/env -S Rscript --vanilla

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
    sum()
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
    sum(na.rm = TRUE)
}

argv <- argparser::arg_parser(
  name = "main.R",
  description = paste(
    "Advent of Code 2024, Day 1:",
    "Take input file containing raw text input, and",
    "print out solution to either part 1 or part 2."
  ),
  hide.opts = TRUE
) |>
  argparser::add_argument(
    arg = "input",
    help = "Input text file path."
  ) |>
  argparser::add_argument(
    arg = "part",
    help = "Which part to solve, either 1 or 2.",
    type = "integer"
  ) |>
  argparser::parse_args()

input <- argv$input |>
  read_input()

argv$part |>
  switch(
    input |> part1() |> cat(sep = "\n"),
    input |> part2() |> cat(sep = "\n")
  )
