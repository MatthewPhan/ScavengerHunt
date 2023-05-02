function openModal(location, location_description, location_image) {

    Swal.fire({
        title: location,
        text: location_description,
        imageUrl: "/media/" + location_image,
        imageWidth: 400,
        imageHeight: 200,
        imageAlt: 'Custom image',
      })

}
