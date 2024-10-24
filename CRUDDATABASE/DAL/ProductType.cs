using System;
using System.Collections.Generic;

namespace CRUDDATABASE.DAL;

public partial class ProductType
{
    public int IdproductType { get; set; }

    public string NameType { get; set; } = null!;

    public virtual ICollection<ProductUser> ProductUsers { get; set; } = new List<ProductUser>();

    public virtual ICollection<Product> Products { get; set; } = new List<Product>();
}
