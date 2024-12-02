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
    purrr::pluck("TRUE") |>
    print()
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
        } else {
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
    }
    TRUE
  }

  input |>
    purrr::map_lgl(is_safe) |>
    table() |>
    purrr::pluck("TRUE") |>
    print()
}

input_file <- "2024/02/input.txt"
input <- read_input(input_file)
part1(input)
part2(input)
