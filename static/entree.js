const addWine = () => {
    console.log(event)
      event.preventDefault()
      winesContainer = document.querySelector('#wines-container')
      winesContainer.innerHTML += `
          <label for="wines">Wine Pairing</label>
          <input name="wines" id="wines" />
          <button onclick="addWine()">Add Wine</button><br />`
}

const addAllergen = () => {
      event.preventDefault()
      allergensContainer = document.querySelector('#allergens-container')
      allergensContainer.innerHTML += `
          <label for="allergens">Allergen</label>
          <input name="allergens" id="allergens" />
          <button onclick="addAllergen()">Add Allergen</button><br />`
}