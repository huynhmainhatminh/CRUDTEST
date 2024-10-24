using System;
using System.Collections.Generic;

namespace CRUDDATABASE.DAL;

public partial class QlUser
{
    public int IdUser { get; set; }

    public string NameUser { get; set; } = null!;

    public string Username { get; set; } = null!;

    public string PassUser { get; set; } = null!;

    public string? Phone { get; set; }

    public string? Email { get; set; }

    public string? Facebook { get; set; }

    public string? AccessUser { get; set; }

    public virtual ICollection<ProductUser> ProductUsers { get; set; } = new List<ProductUser>();

    public virtual ICollection<Product> Products { get; set; } = new List<Product>();
}
