using System;
using System.Collections.Generic;

namespace CRUDDATABASE.DAL;

public partial class ProductUser
{
    public int IdproductUser { get; set; }

    public string NameProduct { get; set; } = null!;

    public string? Description { get; set; }

    public string Username { get; set; } = null!;

    public string? ColorProduct { get; set; }

    public string? DestinyProduct { get; set; }

    public string? ImgProduct { get; set; }

    public int? IdproductType { get; set; }

    public virtual ProductType? IdproductTypeNavigation { get; set; }

    public virtual QlUser UsernameNavigation { get; set; } = null!;
}
