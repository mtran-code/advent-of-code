#!/usr/bin/env -S Rscript --vanilla

read_input <- function(input_file) {
  input_file |>
    readr::read_lines(progress = FALSE)
}


part1 <- function(input) {
  transpose <- function(str_vec) {
    str_vec |>
      stringr::str_split_fixed("", n = length(str_vec)) |>
      t() |>
      apply(1, paste0, collapse = "")
  }

  get_diagonals <- function(str_vec) {
    get_diagonal_i <- function(i, str_vec) {
      str_vec[i:length(str_vec)] |>
        stringr::str_split_fixed("", n = length(str_vec)) |>
        diag() |>
        paste0(collapse = "")
    }
    d1 <- 1:(length(str_vec) - 3) |>
      purrr::map_vec(get_diagonal_i, str_vec) |>
      tail(-1)
    d2 <- 1:(length(str_vec) - 3) |>
      purrr::map_vec(get_diagonal_i, transpose(str_vec))
    c(rev(d1), d2)
  }

  count_xmas <- function(str_vec) {
    pattern1 <- "XMAS"
    pattern2 <- "SAMX"
    sum(
      str_vec |> stringr::str_count(pattern1),
      str_vec |> stringr::str_count(pattern2)
    )
  }

  sum(
    input |> count_xmas(),
    input |> transpose() |> count_xmas(),
    input |> get_diagonals() |> count_xmas(),
    input |>
      purrr::map_vec(stringi::stri_reverse) |>
      get_diagonals() |>
      count_xmas()
  )
}


part2 <- function(input) {
  str_mat <- input |>
    stringr::str_split_fixed("", n = length(input))

  is_x_mas <- function(row, col) {
    top_left <- str_mat[row - 1, col - 1]
    top_right <- str_mat[row - 1, col + 1]
    bottom_left <- str_mat[row + 1, col - 1]
    bottom_right <- str_mat[row + 1, col + 1]

    cross_str <- paste0(top_left, top_right, bottom_left, bottom_right)
    valid_str <- c("MMSS", "MSMS", "SSMM", "SMSM")

    if (cross_str %in% valid_str) {
      TRUE
    } else {
      FALSE
    }
  }

  res <- 0
  for (row in 2:(length(input) - 1)) {
    for (col in 2:(length(input) - 1)) {
      if (str_mat[row, col] == "A" && is_x_mas(row, col)) {
        res <- res + 1
      }
    }
  }
  res
}

argv <- argparser::arg_parser(
  name = "main.R",
  description = paste(
    "Advent of Code 2024, Day 4:",
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
