generate_files <- function(
    year = 2015,
    day = "all", exts = c("py", "R"), templates_path = fs::path("templates")) {
  templates_path |>
    fs::dir_ls(regexp = glue::glue(
      ".*\\/main\\.({stringr::str_c(exts, collapse = '|')})$"
    )) |>
    tibble::as_tibble_col(column_name = "template_file") |>
    dplyr::mutate(base_file = fs::path_file(template_file)) |>
    dplyr::cross_join(tibble::tibble(
      dest_folder = fs::path(year) |>
        fs::dir_create() |>
        fs::path(
          (if (day == "all") {
            1:25
          } else {
            day
          }) |> stringr::str_pad(width = 2, side = "left", pad = "0")
        ) |>
        fs::dir_create() |>
        fs::path("input", ext = "txt") |>
        fs::file_create() |>
        fs::path_dir()
    )) |>
    dplyr::mutate(dest_file = fs::path(dest_folder, base_file)) |>
    dplyr::select(template_file, dest_file) |>
    purrr::pwalk(
      \(template_file, dest_file) {
        fs::file_copy(template_file, dest_file)
      }
    )
}

generate_files(
  year = lubridate::now() |> lubridate::year(),
  day = lubridate::now() |> lubridate::day()
)
