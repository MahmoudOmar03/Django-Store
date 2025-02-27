async function cartUpdate(e) {
  const { data } = await axios(e.dataset.url)
  const { message, items_count } = data
  notyf.success({
    message,
    dismissible: true,
    icon: false,
  })
  document.getElementById('card-items-count').innerHTML = items_count
}

async function cartRemove(e) {
  await axios.get(e.dataset.url)
  location.reload()
}

function switchPaymentMethod(type, content) {
  const stripeCard = document.getElementById('stripe-card');
  const stripePaymentElement = document.getElementById('payment-element');
  const paypalCard = document.getElementById('paypal-card');
  if (type === 'stripe') {
      paypalCard.style.display = 'none'
      stripeCard.style.display = 'block'
      paypalCard.innerHTML = ''
  } else {
      stripeCard.style.display = 'none'
      paypalCard.style.display = 'block'
      stripePaymentElement.innerHTML = ''
      paypalCard.innerHTML = content
  }
}