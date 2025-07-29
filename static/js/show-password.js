// show-password.js
"use strict";

// Expose a global function matching your onclick handler
function createPassword(inputId, btn) {
  // 1) find the input by ID
  const input = document.getElementById(inputId);
  if (!input) return;

  // 2) toggle its type
  input.type = input.type === "password" ? "text" : "password";

  // 3) find the <i> inside the button
  const icon = btn.querySelector("i");
  if (!icon) return;

  // 4) swap classes
  if (icon.classList.contains("fa-eye")) {
    icon.classList.replace("fa-eye", "fa-eye-slash");
  } else {
    icon.classList.replace("fa-eye-slash", "fa-eye");
  }
}

// Keep the old lowercase alias too, in case any markup still uses it
window.createpassword = createPassword;
