provider "packet" {
        auth_token = "${var.auth_token}"
}

resource "packet_project" "development_environment" {
        name = "My Development Instance"
}

