/* Tương tác của bản mẫu khu quản trị.
 * Nút thao tác chưa ghi dữ liệu: hiện thông báo nói rõ khi chạy thật thao tác ghi vào bảng nào
 * (Phụ lục C.10) và cập nhật nhãn trạng thái trên trang để hình dung luồng làm việc.
 * Khi .app có data-mode="static" (bản xuất một tệp để xem thử), các màn hình nằm chung một
 * tệp và chuyển qua lại bằng #địa-chỉ.
 */
(function () {
  "use strict";

  var app = document.querySelector(".app");
  if (!app) return;
  var STATUS_TEXT = { proposed: "Đề xuất", selected: "Đã chọn", dropped: "Đã bỏ", written: "Đã viết", published: "Đã đăng" };
  var toastWrap = document.querySelector(".toast-wrap");

  function toast(title, body) {
    var el = document.createElement("div");
    el.className = "toast";
    var b = document.createElement("b");
    b.textContent = title;
    el.appendChild(b);
    if (body) el.appendChild(document.createTextNode(body));
    toastWrap.appendChild(el);
    setTimeout(function () { el.remove(); }, 6000);
  }

  function setStatus(card, status) {
    document.querySelectorAll('[data-status-for="' + card + '"]').forEach(function (el) {
      el.textContent = STATUS_TEXT[status];
      el.className = "st st-" + status;
    });
    document.querySelectorAll('.card[data-card="' + card + '"]').forEach(function (el) {
      el.dataset.status = status;
    });
    document.querySelectorAll('[data-card-actions="' + card + '"] [data-action]').forEach(function (btn) {
      if (btn.dataset.action === "select") btn.disabled = status !== "proposed";
      if (btn.dataset.action === "drop") btn.disabled = status === "dropped";
    });
  }

  function done(btn, extra) {
    var label = btn.textContent.trim();
    toast("Bản mẫu: " + label, "Khi chạy thật: " + (btn.dataset.note || "") + (extra ? " " + extra : ""));
    if (btn.dataset.card && btn.dataset.newStatus) setStatus(btn.dataset.card, btn.dataset.newStatus);
    if (btn.dataset.hideClosest) {
      var box = btn.closest(btn.dataset.hideClosest);
      if (box) box.hidden = true;
    }
  }

  /* ---------- Hộp thoại xác nhận (confirm() không dùng được trong khung xem thử) */
  var dlg = document.getElementById("dlg-xac-nhan");
  var pending = null;

  function openConfirm(btn) {
    var form = dlg.querySelector("form");
    form.reset();
    dlg.querySelector("[data-title]").textContent = btn.dataset.confirm;
    dlg.querySelector("[data-message]").textContent = btn.dataset.message || "";
    dlg.querySelector("[data-reason-wrap]").hidden = !("reason" in btn.dataset);
    dlg.querySelector("[data-note-wrap]").hidden = !("reason" in btn.dataset || "requireNote" in btn.dataset);
    dlg.querySelector("[data-url-wrap]").hidden = !("url" in btn.dataset);
    dlg.querySelector("[data-err]").hidden = true;
    dlg.querySelector("[data-confirm-label]").textContent = btn.dataset.confirm;
    pending = btn;
    dlg.showModal();
  }

  dlg.querySelector("form").addEventListener("submit", function (e) {
    e.preventDefault();
    var btn = pending;
    var form = e.target;
    var err = dlg.querySelector("[data-err]");
    var reason = form.reason.value;
    var note = form.note.value.trim();
    var msg = "";
    if ("reason" in btn.dataset && !reason) msg = "Chọn một lý do bỏ thẻ.";
    else if ("reason" in btn.dataset && reason === "other" && !note) msg = "Lý do Khác cần ghi chú.";
    else if ("requireNote" in btn.dataset && !note) msg = "Thao tác này cần ghi chú.";
    else if ("url" in btn.dataset) {
      try {
        var host = new URL(form.web_url.value).hostname.replace(/^www\./, "");
        if (host !== "luatsunam.com") msg = "Link bài chính phải thuộc luatsunam.com.";
      } catch (_) { msg = "Nhập link đầy đủ, bắt đầu bằng https://"; }
    }
    if (msg) { err.textContent = msg; err.hidden = false; return; }
    dlg.close();
    var extra = reason ? "Lý do: " + form.reason.options[form.reason.selectedIndex].text + "." : "";
    done(btn, extra);
  });

  document.querySelectorAll("dialog [data-close]").forEach(function (b) {
    b.addEventListener("click", function () { b.closest("dialog").close(); });
  });

  /* ---------- Nút thao tác */
  document.addEventListener("click", function (e) {
    var open = e.target.closest("[data-open]");
    if (open) {
      var d = document.getElementById(open.dataset.open);
      if (d) d.showModal();
      return;
    }
    var copy = e.target.closest("[data-copy]");
    if (copy) {
      e.preventDefault();
      var text = copy.dataset.copy;
      var ok = function () { toast("Đã sao chép", text); };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(ok, function () { toast("Không sao chép được", "Chọn và sao chép tay: " + text); });
      } else {
        toast("Không sao chép được", "Chọn và sao chép tay: " + text);
      }
      return;
    }
    var jump = e.target.closest("[data-jump]");
    if (jump) {
      var scope = jump.closest("[data-view]") || document;
      var to = scope.querySelector('[data-anchor="' + jump.dataset.jump + '"]');
      if (to) to.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "start" });
      return;
    }
    var btn = e.target.closest("button[data-action]");
    if (!btn || btn.disabled) return;
    e.preventDefault();
    if (btn.dataset.confirm) openConfirm(btn);
    else done(btn);
  });

  var away = document.querySelector("[data-away]");
  if (away) away.addEventListener("change", function () {
    toast(away.checked ? "Bản mẫu: bật chế độ vắng mặt" : "Bản mẫu: tắt chế độ vắng mặt",
      "Khi chạy thật: hệ thống vẫn chạy, bản tin vẫn gửi Gmail, Telegram chỉ gửi tin Khẩn. Ghi vào users, activity_log.");
  });

  /* ---------- Ô "+ Dán link" */
  var allowed = (app.dataset.allowedDomains || "").split(",").filter(Boolean);
  var dlForm = document.querySelector('[data-form="dan-link"]');
  if (dlForm) {
    var urlInput = dlForm.querySelector("#dl-url");
    var dlErr = dlForm.querySelector("[data-err]");
    var platform = dlForm.querySelector("#dl-platform");
    var check = function () {
      var v = urlInput.value.trim();
      if (!v) { dlErr.hidden = true; return null; }
      var host;
      try { host = new URL(v).hostname.replace(/^www\.|^m\./, ""); } catch (_) { return "Link chưa đúng dạng; dán link đầy đủ, bắt đầu bằng https://"; }
      if (/^(bit\.ly|tinyurl\.com|t\.co|goo\.gl|shorturl\.at)$/.test(host)) return "Link rút gọn không được chấp nhận; dán link gốc của bài.";
      var ok = allowed.some(function (d) { return host === d || host.endsWith("." + d); });
      if (!ok) return "Tên miền " + host + " chưa có trong danh sách tên miền hoặc danh sách trắng.";
      if (/facebook\.com|fb\.watch/.test(host)) platform.value = "facebook";
      else if (/tiktok\.com/.test(host)) platform.value = "tiktok";
      else if (/youtube\.com|youtu\.be/.test(host)) platform.value = "youtube";
      else if (/vnexpress|tuoitre|thanhnien|nld|plo|baochinhphu|daibieunhandan|baophapluat/.test(host)) platform.value = "press";
      return "";
    };
    urlInput.addEventListener("input", function () {
      var m = check();
      dlErr.textContent = m || "";
      dlErr.hidden = !m;
    });
    dlForm.addEventListener("submit", function (e) {
      e.preventDefault();
      var m = check();
      if (m === null) m = "Dán link cần theo dõi.";
      if (m) { dlErr.textContent = m; dlErr.hidden = false; return; }
      dlForm.closest("dialog").close();
      toast("Bản mẫu: đã nhận link", "Khi chạy thật: lưu tín hiệu, chạy kiểm tra đầu vào; trùng link đã có thì mở bản ghi cũ. Ghi vào manual_signals, activity_log.");
      dlForm.reset();
    });
  }

  /* ---------- Biểu mẫu minh họa (đăng nhập) */
  document.querySelectorAll("[data-demo-form]").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      toast("Bản mẫu", "Khi chạy thật: kiểm tra mật khẩu (Argon2) và mã OTP; ghi activity_log (login_ok, login_fail, otp_fail).");
    });
  });

  /* ---------- Xem trước tệp CSV từ khóa */
  document.querySelectorAll("[data-csv-preview]").forEach(function (input) {
    input.addEventListener("change", function () {
      var out = input.closest(".panel").querySelector("[data-csv-result]");
      var file = input.files && input.files[0];
      if (!file) return;
      var reader = new FileReader();
      reader.onload = function () {
        var lines = String(reader.result).split(/\r?\n/).filter(function (l) { return l.trim(); });
        var head = (lines[0] || "").toLowerCase();
        var kind = /impressions|lượt hiển thị|clicks/.test(head) ? "Search Console"
          : /avg\. monthly searches|searches/.test(head) ? "Keyword Planner"
          : /week|tuần|day|ngày/.test(head) ? "Google Trends" : "chưa nhận ra";
        out.textContent = "Xem trước: " + Math.max(lines.length - 1, 0) + " dòng số liệu, loại tệp " + kind + ". Bản mẫu chưa lưu; khi chạy thật bấm Lưu mới ghi vào keyword_metrics.";
        out.hidden = false;
      };
      reader.readAsText(file);
    });
  });

  /* ---------- Lọc tại chỗ */
  function norm(s) {
    return String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/đ/g, "d");
  }
  document.querySelectorAll("form[data-filter]").forEach(function (form) {
    form.addEventListener("submit", function (e) { e.preventDefault(); });
    var apply = function () {
      var q = norm(form.q && form.q.value);
      var items = form.dataset.filter === "cards"
        ? (form.closest("[data-view]") || document).querySelectorAll(".card[data-card]")
        : document.querySelectorAll(form.dataset.target + " tbody tr");
      items.forEach(function (el) {
        var show = !q || norm(el.dataset.text).indexOf(q) !== -1;
        ["type", "status", "unit", "kind", "group", "label"].forEach(function (k) {
          if (form[k] && form[k].value && el.dataset[k] !== form[k].value) show = false;
        });
        if (form.rising && form.rising.checked && !el.dataset.rising) show = false;
        if (form.outdated && form.outdated.checked && !el.dataset.outdated) show = false;
        el.hidden = !show;
      });
    };
    form.addEventListener("input", apply);
    form.addEventListener("change", apply);
  });

  /* ---------- Bản xuất một tệp: chuyển màn hình bằng #địa-chỉ */
  if (app.dataset.mode === "static") {
    var views = document.querySelectorAll("[data-view]");
    var show = function () {
      var token = decodeURIComponent(location.hash.slice(1)) || "hom-nay";
      var target = document.querySelector('[data-view="' + token + '"]') || document.querySelector('[data-view="hom-nay"]');
      views.forEach(function (v) { v.hidden = v !== target; });
      var section = target.dataset.nav;
      document.querySelectorAll(".nav-item").forEach(function (a) {
        a.classList.toggle("is-active", a.dataset.nav === section);
      });
      if (target.dataset.title) document.title = target.dataset.title;
      window.scrollTo(0, 0);
    };
    window.addEventListener("hashchange", show);
    show();
  }
})();
