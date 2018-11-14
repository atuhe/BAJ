
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
            url: "/report/",
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
                console.log(formData.closingReading)
                // $("textarea#assessment").val('').end();
                // window.location.reload(true);
            }
        });

}