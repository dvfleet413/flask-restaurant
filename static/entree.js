const addWine = () => {
    event.preventDefault()
    const newField = document.createElement('div')
    newField.innerHTML = `
        <label for="wines">Wine Pairing</label>
        <input name="wines" id="wines" />
        <button onclick="addWine()">Add Wine</button><br />`
    document.querySelector('#wines-container').appendChild(newField)
}

const addAllergen = () => {
    event.preventDefault()
    const newField = document.createElement('div')
    newField.innerHTML = `
        <label for="allergens">Allergen</label>
        <input name="Allergens" id="allergens" />
        <button onclick="addAllergen()">Add Allergen</button><br />`
    document.querySelector('#allergens-container').appendChild(newField)
}