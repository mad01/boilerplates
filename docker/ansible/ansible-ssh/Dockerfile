FROM ubuntu:14.04

# install ssh service
RUN apt-get update && apt-get upgrade -y && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:foobar' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# install ansible
RUN apt-get install -y python-yaml python-jinja2 python-httplib2 python-keyczar python-paramiko python-setuptools python-pkg-resources git python-pip
RUN pip install ansible

RUN mkdir -p /etc/ansible
RUN echo '[local]\nlocalhost\n' > /etc/ansible/hosts

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
