#!/usr/bin/env -S Rscript --vanilla

read_input <- function(input_file) {
  input_file |>
    readr::read_lines(progress = FALSE)
}

part1 <- function(input) {
  # CODE HERE
  1
}


part2 <- function(input) {
  # CODE HERE
  1
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
