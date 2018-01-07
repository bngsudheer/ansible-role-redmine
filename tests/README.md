## Running  the test

```sh
sudo container_id=$(date +%s) distro=centos7 playbook=test.yml ./tests/test.sh
```
## Running without removing the container

```sh
sudo cleanup=false container_id=$(date +%s) distro=centos7 playbook=test.yml ./tests/test.sh
```
# About this test
The test is modeled after [Jeff Geerling's blog post](https://www.jeffgeerling.com/blog/testing-ansible-roles-travis-ci-github).
