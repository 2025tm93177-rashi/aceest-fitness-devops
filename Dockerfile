FROM rockylinux:9

# Install Python and dependencies on Rocky Linux
RUN dnf install -y python3 python3-pip && \
    dnf clean all

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python3", "app.py"]
