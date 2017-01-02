resource "packet_project" "development_environment" {
        name = "My Development Instance"
}

resource "packet_device" "unicorn" {
        hostname = "unicorn"
        plan = "baremetal_1"
        facility = "ams1"
        operating_system = "ubuntu_16_04"
        billing_cycle = "hourly"
        project_id = "${packet_project.development_environment.id}"
}
