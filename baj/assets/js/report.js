
function addButton() {
    const pump = document.querySelector('#pumpId').value;
    const openingReading = document.getElementById('openingReadingId').value;
    const closingReading = document.getElementById('closingReadingId').value;
    const transfers = document.getElementById('transfersId').value;
    const meterMovement = parseFloat(openingReading) - parseFloat(closingReading);
    const netSales = parseFloat(meterMovement) + parseFloat(transfers);

    let formValues = {};
    formValues.pump = pump;
    formValues.openingReading = openingReading;
    formValues.closingReading = closingReading;
    formValues.meterMovement = meterMovement;
    formValues.transfers = transfers;
    formValues.netSales = netSales;

    saveReport(formValues)
}

function saveReport(formData) {
    let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        type: "POST",
        url: "/readings/",
        dataType: "json",
            data: {
                pump: formData.pump,
                openingReading: formData.openingReading,
                closingReading: formData.closingReading,
                meterMovement: formData.meterMovement,
                transfers: formData.transfers,
                netSales: formData.netSales,
                csrfmiddlewaretoken: csrftoken
            },
            success:function(data){
                // $("textarea#assessment").val('').end();
                window.location.reload(true);
            }
        });

}

function tankReadingsBtn() {
    const product = document.querySelector('#productId').value;
    const openingStock = parseFloat(document.getElementById('openingStock').value);
    const closingStock = parseFloat(document.getElementById('closingStock').value);
    const productReceived = parseFloat(document.getElementById('productReceived').value);
    const productReturned = parseFloat(document.getElementById('productReturned').value);

    let formValues = {};
    formValues.product = product;
    formValues.openingStock = openingStock;
    formValues.closingStock = closingStock;
    formValues.productReceived = productReceived;
    formValues.productReturned = productReturned;

    saveTankReadings(formValues)
}

function saveTankReadings(formData) {
    let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        type: "POST",
        url: "/readings/tank/",
        dataType: "json",
            data: {
                product: formData.product,
                openingStock: formData.openingStock,
                closingStock: formData.closingStock,
                productReceived: formData.productReceived,
                productReturned: formData.productReturned,
                csrfmiddlewaretoken: csrftoken
            },
            success:function(data){
                // $("textarea#assessment").val('').end();
                window.location.reload(true);
            }
        });
}