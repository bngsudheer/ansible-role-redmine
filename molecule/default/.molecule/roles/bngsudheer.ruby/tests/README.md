# Ansible Role tests

To run the test playbook(s) in this directory:

  1. Install and start Docker.
  1. cd .. (cd to the root directory of this role)
  1. Download the test shim (see .travis.yml file for the URL) into `tests/test.sh`:
  ```sh
    wget -O tests/test.sh https://gist.githubusercontent.com/geerlingguy/73ef1e5ee45d8694570f334be385e181/raw/
  ```
  1. Make the test shim executable:
  ```sh
  chmod +x tests/test.sh
  ```
  1. Run one of the below test commands:

    * Running  the test
```sh
sudo container_id=$(date +%s) distro=centos7 playbook=test.yml ./tests/test.sh
```
    * Running without removing the container
```sh
sudo cleanup=false container_id=$(date +%s) distro=centos7 playbook=test.yml ./tests/test.sh
```