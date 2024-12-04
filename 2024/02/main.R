#!/usr/bin/env -S Rscript --vanilla

read_input <- function(input_file) {
  input_file |>
    readr::read_lines(progress = FALSE)
}

part1 <- function(input) {
  is_safe <- function(input_str) {
    input_ints <- input_str |>
      stringr::str_split_1(" ") |>
      as.integer()
    direction <- ifelse(input_ints[length(input_ints)] > input_ints[1], 1, -1)
    for (i in 2:length(input_ints)) {
      diff <- (input_ints[i] - input_ints[i - 1]) * direction
      if (diff < 1 || diff > 3) {
        return(FALSE)
      }
    }
    TRUE
  }

  input |>
    purrr::map_lgl(is_safe) |>
    table() |>
    purrr::pluck("TRUE")
}


part2 <- function(input) {
  is_safe <- function(input_str, last_chance = FALSE) {
    input_ints <- input_str |>
      stringr::str_split_1(" ") |>
      as.integer()
    direction <- ifelse(input_ints[length(input_ints)] > input_ints[1], 1, -1)
    for (i in 2:length(input_ints)) {
      diff <- (input_ints[i] - input_ints[i - 1]) * direction
      if (diff < 1 || diff > 3) {
        if (last_chance) {
          return(FALSE)
        }
        return(
          is_safe(
            paste(input_ints[-(i - 1)], collapse = " "),
            last_chance = TRUE
          ) || is_safe(
            paste(input_ints[-i], collapse = " "),
            last_chance = TRUE
          )
        )
      }
    }
    TRUE
  }

  input |>
    purrr::map_lgl(is_safe) |>
    table() |>
    purrr::pluck("TRUE")
}

argv <- argparser::arg_parser(
  name = "main.R",
  description = paste(
    "Advent of Code 2024, Day 2:",
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
