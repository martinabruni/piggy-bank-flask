export async function postFormData(path, form, token) {
  const formData = new FormData(form);
  return fetch(path, {
    method: "POST",
    headers: {
      "X-CSRF-Token": token,
      Accept: "application/JSON",
    },
    body: formData,
  })
    .then((response) => {
      return response.json();
    })
    .catch((error) => {
      console.error("Error during login:", error);
      alert("An error occurred. Please try again later.");
    });
}

export async function getData(path) {
  return fetch(path, {
    method: "GET",
    headers: {
      Accept: "application/JSON",
    },
  })
    .then((response) => {
      return response.json();
    })
    .catch((error) => {
      console.error("Error during rendering page:", error);
      alert("An error occurred. Please try again later.");
    });
}

export function handleMessages(message) {
  if (typeof message === "string") {
    alert(message);
    return;
  }

  if (Array.isArray(message)) {
    if (message.length > 0) {
      alert(message[0]);
    }
    return;
  }

  if (typeof message === "object" && message !== null) {
    for (const [key, value] of Object.entries(message)) {
      if (Array.isArray(value) && value.length > 0) {
        alert(`${key}: ${value[0]}`);
      } else {
        alert(`${key}: ${value}`);
      }
      return;
    }
  } else {
    alert("An unknown error occurred.");
  }
}

export function changeTemplate(path) {
  window.location.href = path;
}

export async function register(form, token) {
  var data = await postFormData("/register", form, token);
  if (data.success) {
    renderProfile();
  } else {
    handleMessages(data.message);
  }
}

export async function login(form, token) {
  var data = await postFormData("/login", form, token);
  if (data.success) {
    renderProfile();
  } else {
    handleMessages(data.message);
  }
}

export async function renderProfile() {
  changeTemplate("/html/profile");
}
